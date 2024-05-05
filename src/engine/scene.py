from abc import ABC, abstractmethod

import pygame

from engine.scene_manager import scene_manager
from ui.color import Color


class Scene(ABC):
    def __init__(self, screen, scenes, background_color=Color.BLACK):
        self._screen = screen
        self._scenes = scenes
        self._background_color = background_color
        self._is_started = False
        self._scene_objects = []

    def start(self):
        scene_manager.start_scene(self)

    @property
    def current_time(self):
        return pygame.time.get_ticks()

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def update(self, current_time, events):
        pass

    def render(self):
        self._screen.fill(self._background_color)

        for game_object in self._scene_objects:
            game_object.render(self._screen)

        pygame.display.flip()
