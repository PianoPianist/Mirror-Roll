import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (169, 50, 52)
BLUE = (0, 0, 255)
LIGHTRED = (191, 52, 52)
GREY = (129, 129, 129)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
CYAN = (81, 223, 210)

pygame.init()
# Set the height and width of the screen
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
bgmusic = pygame.mixer.music.load("music.ogg")
pygame.mixer.music.play(300)

class SpriteSheet(object):
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height, colour):
        image = pygame.Surface([width, height]).convert()
        image.set_colorkey(colour)
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image

class Skeleton(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
        super().__init__()
        sprite_sheet = SpriteSheet("enemy.png")
        self.image = sprite_sheet.get_image(0, 0, 64, 64, LIGHTRED)
        self.image = pygame.transform.scale(self.image, [32, 32])
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
 
        # List of sprites we can bump against
        self.level = None
 
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .47
        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
        """ Called when user hits 'jump' button. """
 
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
 
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = 6
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = -6
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
        super().__init__()
        sprite_sheet = SpriteSheet("Player (1).png")
        self.image = sprite_sheet.get_image(0, 0, 64, 64, BLACK)
        self.image = pygame.transform.scale(self.image, [32, 32])
        self.rect = self.image.get_rect()
        
    
 
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
 
        # List of sprites we can bump against
        self.level = None
 
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .47
        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
        """ Called when user hits 'jump' button. """
 
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
 
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
class Lives(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        sprite_sheet = SpriteSheet("Heart_icon.png")
        self.image = sprite_sheet.get_image(0, 0, 27, 27, GREY)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 60

class Portal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        sprite_sheet = SpriteSheet("portal.png")
        self.image = sprite_sheet.get_image(0, 100, 118, 197, BLACK)
        self.image = pygame.transform.scale(self.image, [72, 72])
        self.rect = self.image.get_rect()
class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
 
class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    def __init__(self, skeleton, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.skeleton = skeleton
        self.player = player
         
        # Background image
        self.background = None
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

 
# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, skeleton, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, skeleton, player)
 
        # Array with width, height, x, and y of platform        
        level = [[59, 500, 0, 0],
                 [1000-59, 56, 59, 0],
                 [59, 500, 1000-59, 0],
                 [1000, 59, 0, 500-55],
                 [185, 56, 0, 278],
                 [3, 26, 185, 284],
                 [62, 59, 188, 278+56],
                 [55, 59*4+42, 317, 0],
                 [68, 56, 188+61, 59*3-10],
                 [62*4, 120, 317+60, 334],
                 [62*2+3, 56, 814, 278],
                 [62, 56, 750, 334],
                 [55, 56*3, 567, 56],
                 [62*2+2, 56, 622, 167],
                 [55, 56, 629, 223],
                 ]
        
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.skeleton = self.skeleton
            block.player = self.player
            self.platform_list.add(block)
class Level_02(Level):
    """ Definition for level 1. """
 
    def __init__(self, skeleton, player):
        """ Create level 1. """
        # Call the parent constructor
        Level.__init__(self, skeleton, player)
        # Array with width, height, x, and y of platform        
        level = [[59, 500, 0, 0],
                 [1000-59, 56, 59, 0],
                 [59, 500, 1000-59, 0],
                 [1000, 59, 0, 500-55],
                 [310, 56, 0, 167],
                 [130, 53, 817, 171],
                 [183, 50, 503, 395],
                 [58*4+13, 54, 378, 224],
                 [55, 56, 379, 278],
                 [58, 55, 690, 169],
                 ]
        
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.skeleton = self.skeleton
            block.player = self.player
            self.platform_list.add(block)

class Level_03(Level):
    """ Definition for level 1. """
 
    def __init__(self, skeleton, player):
        """ Create level 1. """
        # Call the parent constructor
        Level.__init__(self, skeleton, player)
        # Array with width, height, x, and y of platform        
        level = [[59, 500, 0, 0],
                 [1000-59, 56, 59, 0],
                 [59, 500, 1000-59, 0],
                 [1000, 59, 0, 500-55],
                 [802-623, 55, 628, 280],
                 [809-753, 112, 753, 333],
                 [433-190, 273-226+6, 192, 226],
                 [247-192, 444-276, 192, 278],
                 [58, 53, 815, 337],
                 [58, 53, 127, 337],
                 [58, 53, 876, 227],
                 [58, 53, 65, 227],
                 [58, 53, 253, 113],
                 [747-692, 163-56, 692, 56],
                 ]
        
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.skeleton = self.skeleton
            block.player = self.player
            self.platform_list.add(block)


class Level_04(Level):
    """ Definition for level 1. """
 
    def __init__(self, skeleton, player):
        """ Create level 1. """
        # Call the parent constructor
        Level.__init__(self, skeleton, player)
        # Array with width, height, x, and y of platform        
        level = [[59, 500, 0, 0],
                 [1000-59, 56, 59, 0],
                 [59, 500, 1000-59, 0],
                 [1000, 59, 0, 500-55],
                 [183-59, 55, 59, 279],
                 [941-815, 443-282, 815, 333],
                 [872-813, 334-281, 815, 281],
                 [683-564, 332-278, 565, 280],
                 [941-750, 54, 750, 170],
                 [246-191, 163-52, 192, 56],
                 [66, 54, 127, 114],
                 [371-316, 223-55, 317, 55],
                 [559-504, 167-56, 504, 56],
                 [121, 49, 500, 336],
                 ]
        
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.skeleton = self.skeleton
            block.player = self.player
            self.platform_list.add(block)

class Level_05(Level): 
    def __init__(self, skeleton, player):
        Level.__init__(self, skeleton, player)
        level = [[47, 200, 0, 0],
                 [1000-59, 49, 59, 0],
                 [59, 500, 954, 0],
                 [1000, 59, 0, 458],
                 [247, 700, 0, 213],
                 [43, 413-41, 303, 41],
                 [953-704, 209-41, 704, 41],
                 [644-404, 413-376, 404, 378],
                 [396-346, 41, 346, 291],
                 [496-454, 375-211, 454, 211],
                 [300, 40, 346, 126],
                 [397-335, 207-166, 335, 166],
                 [647-603, 414-166, 603, 166],
                 [895-700, 42, 703, 251],
                 [42, 124, 855, 292],
                 [45, 71, 704, 345],
                 [110, 41, 748, 376],
                 [50, 41, 496, 250],
                 ]
        
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.skeleton = self.skeleton
            block.player = self.player
            self.platform_list.add(block)
class Level_06(Level): 
    def __init__(self, skeleton, player):
        Level.__init__(self, skeleton, player)
        level = [[46, 500, 0, 0],
                 [1000-59, 49, 59, 0],
                 [59, 500, 954, 0],
                 [1000, 59, 0, 458],
                 [247, 464-210, 754, 210],
                 [300, 40, 46, 293],
                 [45, 37, 202, 254],
                 [295, 208, 0, 0],
                 [50, 39, 701, 295],
                 [84-38, 40, 754, 48],
                 [44, 240, 605, 49],
                 [51, 41, 646, 209],
                 [95, 38, 403, 378],
                 [95, 37, 701, 129],
                 [43, 43, 753, 167],
                 [156, 35, 598, 382],
                 [93, 38, 453, 295],
                 [93, 38, 453, 128],
                 [95, 35, 351, 213],
                 ]
        
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.skeleton = self.skeleton
            block.player = self.player
            self.platform_list.add(block)
def main():
    font = pygame.font.Font("COOPBL.TTF", 30)
    font2 = pygame.font.Font("COOPBL.TTF", 50)
    icon = pygame.image.load("icon.png")
    lvl_2 = pygame.image.load("lvl_2.png")
    lvl_1 = pygame.image.load("lvl_1.png")
    lvl_3 = pygame.image.load("lvl_3.png")
    lvl_4 = pygame.image.load("lvl4.png")
    lvl_5 = pygame.image.load("lvl_5.png")
    lvl_6 = pygame.image.load("lvl6.png")
    win = pygame.image.load("you_win.png")
    opendoc = "yes"
    yes = "yes"
    once = "one"
    yesblit = "no"
    timeone = 0
    time_taken = 0
    lives = 3
    level_list = []
    skeleton = Skeleton()
    player = Player()
    portal = Portal()
    jumpsound = pygame.mixer.Sound("jump.ogg")
    portalsound = pygame.mixer.Sound("portal2.ogg")
    death = pygame.mixer.Sound("death.mp3")
    level_list.append(Level_01(skeleton, player) )
    level_list.append(Level_02(skeleton, player) )
    level_list.append(Level_03(skeleton, player) )
    level_list.append(Level_04(skeleton, player) )
    level_list.append(Level_05(skeleton, player) )
    level_list.append(Level_06(skeleton, player) )
    current_level_no = 0
    current_level = level_list[current_level_no]
    
    lvl_2 = pygame.transform.scale(lvl_2, [1000, 500])
    lvl_1 = pygame.transform.scale(lvl_1, [1000, 500])
    lvl_3 = pygame.transform.scale(lvl_3, [1000, 500])
    lvl_4 = pygame.transform.scale(lvl_4, [1000, 500])
    lvl_5 = pygame.transform.scale(lvl_5, [1000, 500])
    lvl_6 = pygame.transform.scale(lvl_6, [1000, 500])
    win = pygame.transform.scale(win, [1000, 500])
    icon = pygame.transform.scale(icon, [16, 16])
    pygame.display.set_caption("Mirror Roll")
    pygame.display.set_icon(icon)
    heart = Lives()
    heart1 = Lives()
    heart2 = Lives()

    heart.rect.x = 60
    heart1.rect.x = 90
    heart2.rect.x = 120
    
    active_sprite_list = pygame.sprite.Group()
    player_list = pygame.sprite.Group()
    portal_list = pygame.sprite.Group()
    enemy_list = pygame.sprite.Group()
    heart_list = pygame.sprite.Group()

    
    heart_list.add(heart)
    heart_list.add(heart1)

    heart_list.add(heart2)
    
    skeleton.level = current_level
    player.level = current_level
    skeleton.rect.x = 870
    skeleton.rect.y = 231
    player.rect.x = 281
    player.rect.y = 118
    portal.rect.x = 475
    portal.rect.y = 260
    active_sprite_list.add(skeleton)
    active_sprite_list.add(player)
    active_sprite_list.add(portal)
    portal_list.add(portal)
    player_list.add(player)
    enemy_list.add(skeleton)

    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    skeleton.go_left()
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    skeleton.go_right()
                    player.go_right()
                if event.key == pygame.K_UP:
                    skeleton.jump()
                    player.jump()
                    if current_level_no !=7:
                        jumpsound.play()
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and skeleton.change_x > 0:
                    skeleton.stop()
                if event.key == pygame.K_RIGHT and skeleton.change_x < 0:
                    skeleton.stop()
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                    
        screen.fill(CYAN)
        if current_level_no == 0:
            screen.blit(lvl_1, [0, 0])
        if current_level_no == 1:
        
            screen.blit(lvl_2, [0, 0])
            portal.rect.x = 570
            portal.rect.y = 320
            if yes == "yes":
                player.rect.y = 112
                player.rect.x = 79
                skeleton.rect.y = 112
                skeleton.rect.x = 895
                yes = "no"
        if current_level_no == 2:
            screen.blit(lvl_3, [0, 0])
            portal.rect.x = 849
            portal.rect.y = 98
            if yes == "yes":
                player.rect.y = 412
                player.rect.x = 81
                skeleton.rect.y = 409
                skeleton.rect.x = 907
                yes = "no"
        if current_level_no == 3:
            screen.blit(lvl_4, [0, 0])
            portal.rect.x = 627
            portal.rect.y = 208
            if yes == "yes":
                player.rect.y = 214
                player.rect.x = 99
                skeleton.rect.y = 98
                skeleton.rect.x = 849
                yes = "no"
        if current_level_no == 4:
            screen.blit(lvl_5, [0, 0])
            portal.rect.x = 519
            portal.rect.y = 300
            if yes == "yes":
                player.rect.y = 171
                player.rect.x = 158
                skeleton.rect.y = 220
                skeleton.rect.x = 516
                yes = "no"
        if current_level_no == 5:
            screen.blit(lvl_6, [0, 0])
            portal.rect.x = 95
            portal.rect.y = 210
            if yes == "yes":
                player.rect.y = 133
                player.rect.x = 872
                skeleton.rect.y = 389
                skeleton.rect.x = 226
                yes = "no"

        active_sprite_list.update()
        if pygame.sprite.groupcollide(portal_list, player_list, False, False):
            portalsound.play()
            if current_level_no < 5:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
                skeleton.level = current_level
                yes = "yes"
            else:
                current_level_no = 7
                screen.blit(win, [0, 0])
                for i in active_sprite_list:
                    i.kill()
                    
        if pygame.sprite.groupcollide(player_list, enemy_list, False, False):
            death.play()
            lives-=1
            yes = "yes"
            if current_level_no == 0:
                if yes == "yes":
                    skeleton.rect.x = 870
                    skeleton.rect.y = 231
                    player.rect.x = 281
                    player.rect.y = 118
                    yes = "no"
            if current_level_no == 1:        
                if yes == "yes":
                    player.rect.y = 112
                    player.rect.x = 79
                    skeleton.rect.y = 112
                    skeleton.rect.x = 895
                    yes = "no"
            if current_level_no == 2:
                if yes == "yes":
                    player.rect.y = 412
                    player.rect.x = 81
                    skeleton.rect.y = 409
                    skeleton.rect.x = 907
                    yes = "no"
            if current_level_no == 3:
                if yes == "yes":
                    player.rect.y = 214
                    player.rect.x = 99
                    skeleton.rect.y = 98
                    skeleton.rect.x = 849
                    yes = "no"
            if current_level_no == 4:
                if yes == "yes":
                    player.rect.y = 171
                    player.rect.x = 158
                    skeleton.rect.y = 220
                    skeleton.rect.x = 516
                    yes = "no"
            if current_level_no ==5:
                if yes == "yes":
                    player.rect.y = 133
                    player.rect.x = 872
                    skeleton.rect.y = 389
                    skeleton.rect.x = 226
                    yes = "no"
        if pygame.sprite.groupcollide(portal_list, enemy_list, False, False):
            lives-=1
            yes = "yes"
            if current_level_no == 0:
                if yes == "yes":
                    skeleton.rect.x = 870
                    skeleton.rect.y = 231
                    player.rect.x = 281
                    player.rect.y = 118
                    yes = "no"
            if current_level_no == 1:        
                if yes == "yes":
                    player.rect.y = 112
                    player.rect.x = 79
                    skeleton.rect.y = 112
                    skeleton.rect.x = 895
                    yes = "no"
            if current_level_no == 2:
                if yes == "yes":
                    player.rect.y = 412
                    player.rect.x = 81
                    skeleton.rect.y = 409
                    skeleton.rect.x = 907
                    yes = "no"
            if current_level_no == 3:
                if yes == "yes":
                    player.rect.y = 214
                    player.rect.x = 99
                    skeleton.rect.y = 98
                    skeleton.rect.x = 849
                    yes = "no"
            if current_level_no == 4:
                if yes == "yes":
                    player.rect.y = 171
                    player.rect.x = 158
                    skeleton.rect.y = 220
                    skeleton.rect.x = 516
                    yes = "no"
            if current_level_no ==5:
                if yes == "yes":
                    player.rect.y = 133
                    player.rect.x = 872
                    skeleton.rect.y = 389
                    skeleton.rect.x = 226
                    yes = "no"
         #Update items in the level
        current_level.update()
        heart_list.draw(screen)
        # If the player gets near the right side, shift the world left (-x)
        if skeleton.rect.right > SCREEN_WIDTH:
            skeleton.rect.right = SCREEN_WIDTH
        time = font.render("Time: ", True, BLACK)
        level = font.render("Level " + str(current_level_no + 1), True, BLACK)
        screen.blit(time, [60, 95])
        screen.blit(level, [800, 60])
        time_taken = pygame.time.get_ticks()
        time_taken/=1000
        time_taken = round(time_taken, 2)
        high = font2.render("You got a new High Score!!", True, RED)
        # If the player gets near the left side, shift the world right (+x)
        if skeleton.rect.left < 0:
            skeleton.rect.left = 0
            
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left < 0:
            player.rect.left = 0
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        active_sprite_list.draw(screen)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        if lives == 2:
            heart2.kill()
        if lives == 1:
            heart1.kill()
        if lives == 0:
            heart.kill()
            main()
        timetext = font.render(str(time_taken), True, BLACK)
        screen.blit(timetext, [150, 95])
        if current_level_no ==7:
            screen.blit(win, [0, 0])
            if once == "one":
                once = "zero"
                timeone = time_taken
                finaltime = font2.render(str(timeone), True, RED)
                with open("Time.txt", "a+") as doc:
                    doc.seek(0)
                    times = doc.readlines()
                    for i in times:
                        i = float(i)
                        prevhigh = i
                        if time_taken < i:
                            yesblit = "yes"
                            doc.truncate(0)
                            doc.write(str(time_taken))
                            doc.close()
                            prevhigh = time_taken
            lastbest = font2.render(str(prevhigh), True, RED)
            screen.blit (lastbest, [785, 150])
            screen.blit(finaltime, [340, 150])
            if yesblit == "yes":
                yesblit == "no"
                screen.blit(high, [183, 415])
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
 
if __name__ == "__main__":
    main()
