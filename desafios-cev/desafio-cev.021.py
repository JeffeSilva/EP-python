#!/usr/bin/env python
import pygame
#pygame.init() - Problema para iniciar a biblioteca PYGAME não sei bem o por que preciso resolver!
pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
