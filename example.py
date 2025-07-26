import asyncio
from creeper_sound_player import CreeperSoundPlayer

async def main():
    # 创建播放器实例
    player = CreeperSoundPlayer(output_device=2)
    
    # 播放不同类型的音效
    print("播放随机creeper声音...")
    await player.play_random_creeper_sound()
    
    await asyncio.sleep(1)
    
    print("播放爆炸前摇...")
    await player.play_pre_explosion_sound()
    
    await asyncio.sleep(1)
    
    print("播放随机爆炸声音...")
    await player.play_random_explosion_sound()

if __name__ == "__main__":
    asyncio.run(main())