import asyncio

from pyrogram import Client
import tracemalloc
from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from telethon import events
from pytgcalls.types.input_stream import AudioVideoPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from pytgcalls.types.input_stream.quality import HighQualityVideo
from pytgcalls.types.input_stream.quality import LowQualityVideo
from pytgcalls.types.input_stream.quality import LowQualityAudio

from telegram_voice import CMD_HELP,voice_chat_session,auth_session
from dev_install import CHAT_ID
tracemalloc.start()
Debug_mode = True


voice_chat_session.start()
class voice_chat_sessions:
    @auth_session.on(events.NewMessage(outgoing=True, pattern='(?i).*help'))
    async def inline_help(event):
        print(event.raw_text)
        if Debug_mode:
            print('[DEBUG]', event.raw_text)
        await event.respond(
            '''
            **Commands**
            **Streaming Helper**
            .y  -  send a youtube link to stream
                
            ''')


    # https://www.dimensions.com/element/youtube-video-720p
    async def get_youtube_url(YOUTUBE_URL):
        proc = await asyncio.create_subprocess_exec(
            'youtube-dl',
            '-g',
            '-f',
            # CHANGE THIS BASED ON WHAT YOU WANT
            'best[height<=?480][width<=?854]',
            f'{YOUTUBE_URL}',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        return stdout.decode().split('\n')[0]


    @auth_session.on(events.NewMessage(outgoing=True, pattern="^.y (.*)"))
    async def handler(event):
        is_beta = await event.respond("""
        **This is still in beta. It may fail. 
        **

        """)
        
        youtube_url = event.pattern_match.group(1)       
        remote = await voice_chat_sessions.get_youtube_url(youtube_url)
        if_streaming = await event.respond("**if this messages deletes then extracted raw link**")
        
        await auth_session.delete_messages(event.chat_id, [event.id, is_beta.id,if_streaming.id])
        try:
            await voice_chat_session.join_group_call(
                int(CHAT_ID),
                AudioVideoPiped(
                    remote,
                    HighQualityAudio(),
                    HighQualityVideo(),
                ),
                stream_type=StreamType().pulse_stream,
            )
        except Exception as e:
            await event.respond(f"**Error:** `{e}`")
            return
            
        await event.respond(f"**Streaming:**")
        await auth_session.delete_messages(event.chat_id, [event.id, is_beta.id])
        await idle()


    @auth_session.on(events.NewMessage(outgoing=True, pattern="^.stop"))
    async def pause_event(pause_event):
        await voice_chat_session.pause_stream(pause_event.chat_id)
        stopped = await auth_session.send_message(pause_event.chat_id, "**Paused**")
        await auth_session.delete_messages(pause_event.chat_id, [pause_event.id,stopped.id])


    @auth_session.on(events.NewMessage(outgoing=True, pattern="^.resume"))
    async def resume_event(resume_event):
        await voice_chat_session.resume_stream(resume_event.chat_id)
        resumed = await auth_session.send_message(resume_event.chat_id, "**Resumed**")
        await auth_session.delete_messages(resume_event.chat_id, [resume_event.id,resumed.id,])




auth_session.run_until_disconnected()
voice_chat_sessions()



    # handler()
        # await asyncio.sleep(10)
        # await auth_session.delete_messages(event.chat_id, [event.id, is_beta.id])
