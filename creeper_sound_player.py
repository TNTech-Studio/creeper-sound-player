import asyncio
import random
import sounddevice as sd
import soundfile as sf
from pathlib import Path

class CreeperSoundPlayer:
    def __init__(self, sounds_dir="tntsounds", output_device=None):
        self.sounds_dir = Path(sounds_dir)
        self.output_device = output_device
        if output_device is not None:
            sd.default.device = output_device
        
        # 音频文件路径
        self.creeper_sounds = [
            self.sounds_dir / "mob_creeper_say1.mp3",
            self.sounds_dir / "mob_creeper_say2.mp3"
        ]
        
        self.explosion_sounds = [
            self.sounds_dir / "random_explode1.mp3",
            self.sounds_dir / "random_explode3.mp3", 
            self.sounds_dir / "random_explode4.mp3"
        ]
        
        self.pre_explosion_sound = self.sounds_dir / "creeper-pre-explosion-shaking.mp3"

    async def play_random_creeper_sound(self):
        """随机播放creeper声音"""
        sound_file = random.choice(self.creeper_sounds)
        await self._play_sound(sound_file)

    async def play_random_explosion_sound(self):
        """随机播放爆炸声音"""
        sound_file = random.choice(self.explosion_sounds)
        await self._play_sound(sound_file)

    async def play_pre_explosion_sound(self):
        """播放爆炸前摇声音"""
        await self._play_sound(self.pre_explosion_sound)

    async def _play_sound(self, sound_file):
        """异步播放音频文件"""
        def play():
            data, fs = sf.read(str(sound_file))
            # 确保音频数据格式正确
            if len(data.shape) == 1:
                data = data.reshape(-1, 1)
            sd.play(data, fs, device=self.output_device)
            sd.wait()
        
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, play)
    
    @staticmethod
    def list_audio_devices():
        """列出所有可用的音频输出设备"""
        return sd.query_devices()