import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Camera:
    """A simple 3D camera control."""
    def __init__(self, position=(0, 0, 0), rotation=(0, 0)):
        self.position = list(position)
        self.rotation = list(rotation)

    def update(self, dx, dy, dz, drx, dry):
        """Update camera position and rotation."""
        self.position[0] += dx
        self.position[1] += dy
        self.position[2] += dz
        self.rotation[0] += drx
        self.rotation[1] += dry

    def apply(self):
        """Apply camera transformations."""
        glRotatef(self.rotation[0], 1, 0, 0)
        glRotatef(self.rotation[1], 0, 1, 0)
        glTranslatef(-self.position[0], -self.position[1], -self.position[2])

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    gluPerspective(45, (800/600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    camera = Camera(position=(0, 0, 5))

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()

        # Camera movement control
        dx = 0.05 if keys[K_w] else -0.05 if keys[K_s] else 0
        dy = 0.05 if keys[K_SPACE] else -0.05 if keys[K_LSHIFT] else 0
        dz = 0.05 if keys[K_d] else -0.05 if keys[K_a] else 0
        drx = 1 if keys[K_UP] else -1 if keys[K_DOWN] else 0
        dry = 1 if keys[K_RIGHT] else -1 if keys[K_LEFT] else 0

        camera.update(dx, dy, dz, drx, dry)

        # Apply camera transformation
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        camera.apply()

        # Draw objects (simple cube for example)
        glBegin(GL_QUADS)
        for x, y, z in [(1,1,1), (-1,1,1), (-1,-1,1), (1,-1,1)]:
            glVertex3f(x, y, z)
        glEnd()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
