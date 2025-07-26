import asyncio
from creeper_sound_player import CreeperSoundPlayer

async def main():
    # 列出所有音频设备
    print("可用音频设备:")
    devices = CreeperSoundPlayer.list_audio_devices()
    for i, device in enumerate(devices):
        if device['max_output_channels'] > 0:
            print(f"{i}: {device['name']}")
    
    # 选择设备（使用Mac mini Speakers）
    device_id = 2  # 根据上面列表选择
    player = CreeperSoundPlayer(output_device=device_id)
    
    await player.play_random_creeper_sound()

if __name__ == "__main__":
    asyncio.run(main())