import random
import pygame
import os

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, x, y, speed = 0):
        super().__init__()
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.lane = (x - 100) // 200
        
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 800:
            self.kill()
        
class Sedan(Vehicle):
    def __init__(self, lane, speed):
        color = random.choice(['black', 'red', 'yellow'])
        original_image = pygame.image.load(os.path.join('resources', f'sedan_{color}.png')).convert_alpha()
        scale_image = pygame.transform.scale(original_image, (int(original_image.get_width()*0.7), int(original_image.get_height()*0.7)))
        self.image = pygame.transform.rotate(scale_image, 180)
        x = 100 + lane * 200
        super().__init__(x, self.image.get_height()//2, speed)
        
        
class F1(Vehicle):
    def __init__(self):
        original_image = pygame.image.load(os.path.join('resources', 'F1.png')).convert_alpha()
        self.image = pygame.transform.scale(original_image, (int(original_image.get_width()*0.7), int(original_image.get_height()*0.7)))
         
        super().__init__(300, 700)
        
        
    def move_left(self):
        if self.lane > 0:
            self.lane -= 1
            self.rect.centerx = 100 + self.lane * 200
            
    def move_right(self):
        if self.lane < 2:
            self.lane += 1
            self.rect.centerx = 100 + self.lane * 200
    
    
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0
        self.player = F1()
        self.all_sprites = pygame.sprite.Group(self.player)
        self.sedans = pygame.sprite.Group()
        self.lanes = [[], [], []]
        self.last_spawn_time = pygame.time.get_ticks()
        self.spawn_delay = 2000
        self.min_sedan_speed = 3
        self.max_sedan_speed = 7
        self.difficulty_increase = 0
        
    def spawn_sedan(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time > self.spawn_delay:
            available_lanes = [i for i in range(3) if not self.lanes[i]]
            if available_lanes:
                lane = random.choice(available_lanes)
                speed = random.randint(self.min_sedan_speed, self.max_sedan_speed)
                sedan = Sedan(lane, speed)
                self.all_sprites.add(sedan)
                self.sedans.add(sedan)
                self.lanes[lane].append(sedan)
                self.last_spawn_time = current_time
                
    def increase_difficulty(self):
        self.difficulty_increase += 1
        self.min_sedan_speed = 3 + self.difficulty_increase
        self.max_sedan_speed = 7 + self.difficulty_increase
        self.spawn_delay = max(500, 2000 - self.difficulty_increase * 100)
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.player.move_right()
                
    def update(self):
        self.all_sprites.update()
        for lane in self.lanes:
            lane[:] = [sedan for sedan in lane if sedan.alive()]
        self.spawn_sedan()
        if pygame.sprite.spritecollide(self.player, self.sedans, False):
            self.running = False
        self.score += 1
        
        if self.score % 100 == 0:
            self.increase_difficulty()
            
    def draw(self):
        self.screen.fill("white")
        for i in range(3):
            pygame.draw.line(self.screen, "gray", (200 * i, 0), (200 * i, 800), 2)
        self.all_sprites.draw(self.screen)
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, "black")
        self.screen.blit(score_text, (10, 10))
        pygame.display.flip()
        
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()
        
if __name__ == '__main__':
    game = Game()
    game.run()