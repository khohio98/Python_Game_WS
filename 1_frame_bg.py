import pygame
import os
################################################################################################################################
pygame.init()       # 초기화

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀 설정
pygame.display.set_caption("PANG GAME")

#FPS
clock = pygame.time.Clock()
################################################################################################################################

# 1. 사용자 게임 초기화
    # 배경 이미지 불러오기
    # 게임 이미지 불러오기
    # 좌표, 속도, 폰트 

    

current_path = os.path.dirname(__file__)        #현재 파일 위치 반환  
image_path = os.path.join(current_path, "IMGS")

background = pygame.image.load(os.path.join(image_path, "BG.png"))

stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]        #스테이지 높이 위에 캐릭터를 두기위해 사용

character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height




running = True     
while running:
    # FPS 설정
    dt = clock.tick(30)

    # 2. 이벤트 처리(키보드, 마우스 등 입력 값 처리)
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:       
            running = False       

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    # 게임화면을 다시 그리기
    pygame.display.update()     
    

# 종료 전, 게임 대기
# pygame.time.delay(1500)

# 파이 게임 종료
pygame.quit()