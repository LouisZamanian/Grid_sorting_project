import pygame
from grid import Grid
import random
pygame.init()


def creer_matrice(n, m):
    return [[i + j * m + 1 for i in range(m)] for j in range(n)]


def generate_random_grid(m, n):
    numbers = list(range(1, m * n + 1))
    random.shuffle(numbers)
    return [numbers[i:i + n] for i in range(0, len(numbers), n)]

def generate_grids(nb_inf,nb_sup, m, n,dif):
    target_grid = Grid(m, n, [[i + j * n + 1 for i in range(n)] for j in range(m)])
    for i in range(10):
        grid = Grid(m, n, generate_random_grid(m, n))
        neighbor_graph, arretes, noeuds = grid.a_star()
        shortest_path = neighbor_graph.bfs(grid.transform(), target_grid.transform())
        if nb_inf<len(shortest_path)<nb_sup:
            return grid
    if dif=="easy":
        return Grid(2,3,[[6, 4, 3], [2, 1, 5]])
    elif dif=="medium":
        return Grid(3,3,[[1, 6, 2], [5, 8, 3], [4, 7, 9]])
    else:
        return Grid(3,3,[[2, 9, 7], [5, 8, 4], [6, 3, 1]])


# Définir les couleurs
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
#Grid(3,3, [[1,2,3],[4,5,6],[7,8,9]])
L0 = Grid(2,2,[[1, 3], [2, 4]])
L = Grid(3,3,[[1, 2, 5], [3, 4, 6], [9, 7, 8]])
L1=Grid(4,4,[[1,16,14,12],[13,11,10,9],[5,2,8,3],[4,6,7,15]])
#m0, n0 = L0.m, L0.n
#m, n = L.m, L.n
#m1, n1 = L1.m, L1.n
size = 100

#creation swap interdits


def swap_fb(m, n, level):
    swap_fb = []

    if level == "easy":
        swap_fb = [[(1, 1), (1, 2)]]
    elif level == "medium":
        swap_fb = [[(1, 1), (1, 2)]]
    else:
        swap_fb = [[(1, 1), (1, 2)], [(2, 3), (3, 3)]]

    return swap_fb



# Définir la taille de la fenêtre une seule fois en dehors de la boucle
screen_width = (5 + 1) * size
screen_height = (5 + 1) * size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Écran d'accueil")

# Définir la police de texte
font = pygame.font.SysFont("Arial", 30)

# Définir les boutons
buttons = [
    {"text": "Easy", "level": "easy", "rect": pygame.Rect(100, 100, 200, 50)},
    {"text": "Medium", "level": "medium", "rect": pygame.Rect(100, 200, 200, 50)},
    {"text": "Hard", "level": "hard", "rect": pygame.Rect(100, 300, 200, 50)},
]
toggle_button = {"text": "Swaps interdits", "level": "toggle_swaps", "rect": pygame.Rect(100, 400, 200, 50)}
buttons.append(toggle_button)


text_front = pygame.font.SysFont("Arial", 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_text_rect(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    text_rect = img.get_rect(center=(x, y))
    screen.blit(img, text_rect)

def draw_numbered_box(number, x, y, size):
    pygame.draw.rect(screen, white, (x, y, size, size))
    pygame.draw.rect(screen, black, (x, y, size, size), 2)
    draw_text_rect(str(number), font, black, x + size // 2, y + size // 2)

def is_swap_allowed(selected,target,swap_fb):
    # Ajouter des conditions pour interdire le swap entre certaines cases
    for elt in swap_fb:
        if (selected == elt[0] and target == elt[1]) or (selected == elt[1] and target == elt[0]) :
            return False
    # Ajouter d'autres conditions selon vos besoins

    return True

def create_sorted_grid(m,n):
    return Grid(m,n,[list(range(i *n + 1, (i + 1) * n + 1)) for i in range(m)])
def easy_game(L, size,swap_fb):
    run = True
    m=L.m;n=L.n
    target_grid=create_sorted_grid(m,n)
    neighbor_graph, arretes, noeuds = L.a_star_final_heapq()
    shortest_path = neighbor_graph.bfs(L.transform(), target_grid.transform())
    compt_sol=len(shortest_path)
    selected = None
    compt=0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x0, y0 = event.pos[0], event.pos[1]
                i0 = int(y0 / size - 1 / 2)
                j0 = int(x0 / size - 1 / 2)
                print(x0, y0, i0, j0)
                selected = (i0, j0)

            if event.type == pygame.MOUSEBUTTONUP:
                if selected:
                    x1, y1 = event.pos[0], event.pos[1]
                    i1 = int(y1 / size - 1 / 2)
                    j1 = int(x1 / size - 1 / 2)
                    target=(i1,j1)
                    print(x1, y1, i1, j1)

                    if (abs(i0 - i1) == 1 and j0 == j1) or (abs(j0 - j1) == 1 and i0 == i1):
                        if is_swap_allowed(selected,target,swap_fb):
                            L.swap((i0,j0), (i1,j1))
                            compt+=1

                    selected = None

            if event.type == pygame.QUIT:
                run = False

        screen.fill(white)
        if L.is_sorted():
            draw_text(f"Bravo, tu as résolu le problème en",
                      text_front, (0, 0, 0), 0, screen_height - size )
            draw_text(f"{compt}{' coup alors que la solution ' if compt == 1 else ' coups alors que la solution'}",
                      text_front, (0, 0, 0), 0, screen_height - 2 * size / 3)
            draw_text(f"La solution optimale est en {compt_sol-1} {'coup' if compt_sol == 1 else 'coups'}", text_front,
                      (0, 0, 0), 0, screen_height - size / 3)

        for i in range(m):
            for j in range(n):
                y = i * size + size // 2
                x = j * size + size // 2
                draw_numbered_box(L.state[i][j], x, y, size)
                draw_line(swap_fb,size)


        pygame.display.flip()

        pygame.time.delay(10) # Ajouter un petit délai pour réduire l'utilisation du processeur




def draw_line(swap_fb,size):
    for elt in swap_fb:
        i1=elt[0][0];j1=elt[0][1]
        i2 = elt[1][0];j2 = elt[1][1]
        y1 = i1 * size + size // 2
        x1 = j1 * size + size // 2
        y2 = i2 * size + size // 2
        x2 = j2 * size + size // 2
        if elt[0][0]==elt[1][0]:
            #xi=size*0.5+0.5*(elt[0][0]+elt[1][0]+2)*size;yi=size+(elt[0][1]+elt[1][1])*0.5*size
            xi=(x1+x2)*0.5+size*0.5;yi=(y1+y2)*0.5
            xf=xi;yf=yi+size
            print("barre verticale",xi,yi)
            pygame.draw.line(screen,"red",(xi,yi),(xf,yf),5)
        elif elt[0][1]==elt[1][1]:
            #xi = size // 2 + (elt[0][0] + elt[1][0]) / 2 * size;yi = size + (elt[0][1] + elt[1][1]) / 2 * size
            xi = (x1 + x2) * 0.5 ;yi = (y1 + y2) * 0.5+ size * 0.5
            xf =xi+size ;yf = yi
            pygame.draw.line(screen, "red", (xi, yi), (xf, yf), 5)

def draw_buttons(screen_width, screen_height, swap_fb_enabled):
    # Calculer la position verticale centrale pour les boutons
    center_y = screen_height // 2

    for i, button in enumerate(buttons):
        # Calculer la position horizontale centrale pour les boutons
        center_x = screen_width // 2

        # Décaler chaque bouton verticalement
        vertical_offset = i * 60

        # Ajouter l'offset vertical pour centrer les boutons
        button["rect"].center = (center_x, size + vertical_offset)

        if button["level"] == "toggle_swaps":
            color = (100, 255, 100) if swap_fb_enabled else (255, 100, 100)
        else:
            color = gray

        pygame.draw.rect(screen, color, button["rect"])
        pygame.draw.rect(screen, black, button["rect"], 2)
        text_surface = font.render(button["text"], True, black)
        text_rect = text_surface.get_rect(center=button["rect"].center)
        screen.blit(text_surface, text_rect)


swap_fb_enabled = False  # Initialisation des swaps interdits à désactivés
running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button["rect"].collidepoint(event.pos):
                    if button["level"] == "toggle_swaps":
                        swap_fb_enabled = not swap_fb_enabled
                        if swap_fb_enabled:
                            print("Swaps interdits activés")
                        else:
                            print("Swaps interdits désactivés")
                    elif button["level"] == "easy":
                        swp_fb=swap_fb(2,3,"easy")
                        L0=generate_grids(3,5, 2, 3,"easy")
                        easy_game(L0, size, swp_fb if swap_fb_enabled else [])
                        print(f"Clicked {button['level']} button")
                    elif button["level"] == "medium":
                        swp_fb = swap_fb(3, 3, "medium")
                        L=generate_grids(6,10, 3, 3,"medium")
                        easy_game(L, size, swp_fb if swap_fb_enabled else [])
                        print(f"Clicked {button['level']} button")
                    elif button["level"] == "hard":
                        swp_fb = swap_fb(4, 4, "hard")
                        L1=generate_grids(11,100, 4, 4,"hard")
                        easy_game(L1, size, swp_fb if swap_fb_enabled else [])
                        print(f"Clicked {button['level']} button")

    screen.fill(white)
    draw_buttons(screen_width, screen_height, swap_fb_enabled)
    pygame.display.flip()

# Quitter pygame proprement
pygame.quit()