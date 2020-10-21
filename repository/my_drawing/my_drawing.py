"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect ,GLabel
from campy.graphics.gwindow import GWindow

window = GWindow(width=600, height=800, title='~ Alien ~')


def main():
    """
    Function: Draw the alien of Toy Story
    Principle: Create background, claws, body, buttons, joysticks, text
    """
    back_u_color = 'skyblue'
    back_l_color = 'Orange'

    draw_back(back_u_color, back_l_color)
    paw(60, 0)
    alien(0, 120, back_u_color=back_u_color, back_l_color=back_l_color)
    joystick(290, 580)
    button(120, 580)
    textbox()


def alien(x=0, y=0, main_color='greenyellow', eye_color='black', clothes_color='dodgerblue',back_u_color='white', back_l_color='white'):
    """
    Function: draw alien
    Principle: build face, top, eyes, body, feet, smile
    :param x: x-axis displacement
    :param y: y-axis displacement
    :param back_u_color: upper background color
    :param back_l_color: lower background color
    :param main_color: main color
    :param eye_color: eye color
    :param clothes_color: clothes color
    """

    body(x, y, back_u_color=back_u_color, back_l_color=back_l_color)
    ear(x, y, back_color=back_u_color)
    face(x, y)
    top(x, y)

    feet(x, y, back_l_color=back_l_color)
    smile(x, y)
    eye(x, y)


def draw_back(back_color_up='white', back_color_lower='white'):
    """
    Function: draw a background image
    Principle: layer the upper and lower parts of the background and provide preset values
    :param back_color_up: upper background color
    :param back_color_lower: lower background color
    """
    draw_u = GRect(window.width, window.height)
    draw_u.filled = True
    draw_u.color = back_color_up
    draw_u.fill_color = back_color_up
    window.add(draw_u)

    draw_l = GOval(1400, 500, x=- 110, y=470)
    draw_l.filled = True
    draw_l.color = back_color_lower
    draw_l.fill_color = back_color_lower
    window.add(draw_l)


def ear(dx=0, dy=0, main_color='greenyellow', back_color='white' ):
    """
    Function: draw ears
    Principle: use ellipse subtraction to create curved shape
    :param dx: x-axis displacement
    :param dy: y-axis displacement
    :param back_color: background color
    :param main_color: main color
    """
    l_ear = GOval(80, 150, x=dx+80, y=dy+150)
    l_ear.filled = True
    l_ear.color = main_color
    l_ear.fill_color = main_color
    window.add(l_ear)

    l_ear_x = GOval(40, 140, x=dx+70, y=dy+155)
    l_ear_x.filled = True
    l_ear_x.color = back_color
    l_ear_x.fill_color = back_color
    window.add(l_ear_x)

    r_ear = GOval(80, 150, x=dx+460, y=dy+150)
    r_ear.filled = True
    r_ear.color = main_color
    r_ear.fill_color = main_color
    window.add(r_ear)

    r_ear_x = GOval(40, 140, x=dx+510, y=dy+155)
    r_ear_x.filled = True
    r_ear_x.color = back_color
    r_ear_x.fill_color = back_color
    window.add(r_ear_x)


def face(dx=0, dy=0, main_color='greenyellow', necklace_color='purple'):
    """
    Function: draw face
    Principle: use ellipse subtraction to create curved shape
    :param dx: x-axis displacement
    :param dy: y-axis displacement
    :param main_color: main color
    :param necklace_color: necklace color
    """
    face = GOval(350, 200, x=dx+135, y=dy+135)
    face.filled = True
    face.color = main_color
    face.fill_color = main_color
    window.add(face)

    necklace = GOval(300, 70, x=dx+160, y=dy+270)
    necklace.filled = True
    necklace.color = necklace_color
    necklace.fill_color = necklace_color
    window.add(necklace)

    necklace_x = GOval(330, 100, x=dx+145, y=dy+215)
    necklace_x.filled = True
    necklace_x.color = main_color
    necklace_x.fill_color = main_color
    window.add(necklace_x)


def top(dx=0, dy=0, main_color='greenyellow'):
    """
    Function: draw top
    Principle: use ellipse subtraction to create curved shape
    :param dx: x-axis displacement
    :param dy: y-axis displacement
    :param main_color: main color
    """
    pillar = GOval(30, 200, x=dx+295, y=dy+50)
    pillar.filled = True
    pillar.color = main_color
    pillar.fill_color = main_color
    window.add(pillar)

    ball = GOval(40, 40, x=dx+290, y=dy+40)
    ball.filled = True
    ball.color = main_color
    ball.fill_color = main_color
    window.add(ball)


def eye(dx=0, dy=0, eye_color='black', eye_white_color='white'):
    """
    Function: draw eyes
    Principle: complete with circle
    :param dx: x-axis displacement
    :param dy: y-axis displacement
    :param eye_color: eye color
    :param eye_white_color: white of eye's color
    """
    l_eye_1 = GOval(70, 70, x=dx+170, y=dy+180)
    l_eye_1.filled = True
    l_eye_1.color = eye_white_color
    l_eye_1.fill_color = eye_white_color
    window.add(l_eye_1)

    l_eye_2 = GOval(20, 20, x=dx+200, y=dy+200)
    l_eye_2.filled = True
    l_eye_2.color = eye_color
    l_eye_2.fill_color = eye_color
    window.add(l_eye_2)

    m_eye_1 = GOval(70, 70, x=dx+270, y=dy+165)
    m_eye_1.filled = True
    m_eye_1.color = eye_white_color
    m_eye_1.fill_color = eye_white_color
    window.add(m_eye_1)

    m_eye_2 = GOval(20, 20, x=dx+295, y=dy+185)
    m_eye_2.filled = True
    m_eye_2.color = eye_color
    m_eye_2.fill_color = eye_color
    window.add(m_eye_2)

    r_eye_1 = GOval(70, 70, x=dx+370, y=dy+180)
    r_eye_1.filled = True
    r_eye_1.color = eye_white_color
    r_eye_1.fill_color = eye_white_color
    window.add(r_eye_1)

    r_eye_2 = GOval(20, 20, x=dx+390, y=dy+200)
    r_eye_2.filled = True
    r_eye_2.color = eye_color
    r_eye_2.fill_color = eye_color
    window.add(r_eye_2)


def body(dx=0, dy=0, main_color='greenyellow', clothes_color='dodgerblue', back_u_color='white', back_l_color='white'):
    """
    Function: draw body
    Principle: use ellipse subtraction to create curved shape
    :param dx: x-axis displacement
    :param dy: y-axis displacement
    :param main_color: main color
    :param clothes_color: clothes color
    :param back_u_color: upper background color
    :param back_l_color: lower background color
    """
    l_arm = GOval(280, 300, x=dx+130, y=dy+260)
    l_arm.filled = True
    l_arm.color = clothes_color
    l_arm.fill_color = clothes_color
    window.add(l_arm)

    r_arm = GOval(280, 300, x=dx+210, y=dy+260)
    r_arm.filled = True
    r_arm.color = clothes_color
    r_arm.fill_color = clothes_color
    window.add(r_arm)

    arm_x = GRect(500, 300, x=dx+100, y=dy+450)
    arm_x.filled = True
    arm_x.color = back_l_color
    arm_x.fill_color = back_l_color
    window.add(arm_x)

    l_hand = GOval(70, 70, x=dx+130, y=dy+430)
    l_hand.filled = True
    l_hand.color = main_color
    l_hand.fill_color = main_color
    window.add(l_hand)

    # l_finger = GOval(35, 40, x=dx+155, y=dy+470)
    # l_finger.filled = True
    # l_finger.color = main_color
    # l_finger.fill_color = main_color
    # window.add(l_finger)

    r_hand = GOval(70, 70, x=dx+420, y=dy+430)
    r_hand.filled = True
    r_hand.color = main_color
    r_hand.fill_color = main_color
    window.add(r_hand)

    # r_finger = GOval(35, 40, x=dx+435, y=dy+470)
    # r_finger.filled = True
    # r_finger.color = main_color
    # r_finger.fill_color = main_color
    # window.add(r_finger)

    body = GOval(290, 600, x=dx+165, y=dy+100)
    body.filled = True
    body.color = clothes_color
    body.fill_color = clothes_color
    window.add(body)

    body_x = GRect(300, 300, x=dx+160, y=dy+0)
    body_x.filled = True
    body_x.color = back_u_color
    body_x.fill_color = back_u_color
    window.add(body_x)

    belt = GOval(300, 110, x=dx+160, y=dy+360)
    belt.filled = True
    belt.color = 'navy'
    belt.fill_color = 'navy'
    window.add(belt)

    belt_x = GOval(290, 80, x=dx+165, y=dy+360)
    belt_x.filled = True
    belt_x.color = clothes_color
    belt_x.fill_color = clothes_color
    window.add(belt_x)


def feet(dx=0, dy=0, clothes_color='dodgerblue', feet_color='navy', back_l_color='white'):
    """
    Function: draw feet
    Principle: use ellipse subtraction to create curved shape
    :param dx: x-axis displacement
    :param dy: y-axis displacement
    :param clothes_color: clothes color
    :param feet_color: feet color
    :param back_l_color: lower background color
    """
    l_feet = GOval(160, 130, x=dx+130, y=dy+550)
    l_feet.filled = True
    l_feet.color = feet_color
    l_feet.fill_color = feet_color
    window.add(l_feet)

    r_feet = GOval(160, 130, x=dx+330, y=dy+550)
    r_feet.filled = True
    r_feet.color = feet_color
    r_feet.fill_color = feet_color
    window.add(r_feet)

    feet_x = GRect(500, 500, x=dx + 100, y=dy + 600)
    feet_x.filled = True
    feet_x.color = back_l_color
    feet_x.fill_color = back_l_color
    window.add(feet_x)

    low_body = GOval(260, 130, x=dx+180, y=dy+470)
    low_body.filled = True
    low_body.color = clothes_color
    low_body.fill_color = clothes_color
    window.add(low_body)

    shadow = GOval(100, 50, x=dx+260, y=dy+470)
    shadow.filled = True
    shadow.color = 'black'
    shadow.fill_color = 'black'
    window.add(shadow)

    shadow_x = GOval(120, 47, x=dx+250, y=dy+470)
    shadow_x.filled = True
    shadow_x.color = clothes_color
    shadow_x.fill_color = clothes_color
    window.add(shadow_x)

    shadow = GRect(2, 80, x=dx+307, y=dy+520)
    shadow.filled = True
    shadow.color = 'black'
    shadow.fill_color = 'black'
    window.add(shadow)

    belt = GRect(90, 50, x=dx+265, y=dy+430)
    belt.filled = True
    belt.color = 'navy'
    belt.fill_color = 'navy'
    window.add(belt)


def smile(dx=0, dy=0, main_color='greenyellow'):
    """
    Function: draw smile
    Principle: use ellipse subtraction to create curved shape
    :param dx: x-axis displacement
    :param dy: y-axis displacement
    :param main_color: main color
    """
    smile_line = GOval(220, 70, x=dx+200, y=dy+230)
    smile_line.filled = True
    smile_line.color = 'black'
    smile_line.fill_color = 'black'
    window.add(smile_line)

    smile_x = GOval(220, 67, x=dx+200, y=dy+230)
    smile_x.filled = True
    smile_x.color = main_color
    smile_x.fill_color = main_color
    window.add(smile_x)


def joystick(dx=0, dy=0):
    """
    Function: draw joystick
    Principle: use ellipse subtraction to create curved shape
    :param dx: x-axis displacement
    :param dy: y-axis displacement
    """
    l_joy = GOval(100, 40, x=dx + 40, y=dy + 175)
    l_joy.filled = True
    l_joy.color = 'gray'
    l_joy.fill_color = 'gray'
    window.add(l_joy)

    m_joy = GOval(30, 100, x=dx + 75, y=dy + 100)
    m_joy.filled = True
    m_joy.color = 'black'
    m_joy.fill_color = 'black'
    window.add(m_joy)

    u_joy = GOval(80, 80, x=dx + 50, y=dy + 50)
    u_joy.filled = True
    u_joy.color = 'red'
    u_joy.fill_color = 'red'
    window.add(u_joy)


def button(dx=0, dy=0):
    """
    Function: draw button
    Principle: use ellipse subtraction to create curved shape
    :param dx: x-axis displacement
    :param dy: y-axis displacement
    """
    l_button = GOval(100, 40, x=dx + 40, y=dy + 175)
    l_button.filled = True
    l_button.color = 'gray'
    l_button.fill_color = 'gray'
    window.add(l_button)

    u_button = GOval(100, 40, x=dx + 40, y=dy + 168)
    u_button.filled = True
    u_button.color = 'red'
    u_button.fill_color = 'red'
    window.add(u_button)


def paw(dx=0, dy=0, main_color='gray', back_u_color='skyblue'):
    """
    Function: draw smile
    Principle: use ellipse subtraction to create curved shape
    :param dx: x-axis displacement
    :param dy: y-axis displacement
    :param main_color: main color
    :param back_u_color: upper background color
    """
    paw_catch = GOval(400, 250, x=dx + 40, y=dy + 0)
    paw_catch.filled = True
    paw_catch.color = main_color
    paw_catch.fill_color = main_color
    window.add(paw_catch)

    paw_x = GOval(400, 250, x=dx + 40, y=dy + 20)
    paw_x.filled = True
    paw_x.color = back_u_color
    paw_x.fill_color = back_u_color
    window.add(paw_x)

    l_paw = GOval(15, 45, x=dx + 40, y=dy + 100)
    l_paw.filled = True
    l_paw.color = 'black'
    l_paw.fill_color = 'black'
    window.add(l_paw)

    r_paw = GOval(15, 45, x=dx + 425, y=dy + 100)
    r_paw.filled = True
    r_paw.color = 'black'
    r_paw.fill_color = 'black'
    window.add(r_paw)

    paw_box = GOval(200, 80, x=dx + 140, y=dy - 10)
    paw_box.filled = True
    paw_box.color = 'black'
    paw_box.fill_color = 'black'
    window.add(paw_box)


def textbox(dx=0, dy=0):
    """
    Function: draw text
    Principle: use label
    :param dx: x-axis displacement
    :param dy: y-axis displacement
    """
    txt = GLabel('保夾500元', x=dx + 130, y=dy + 160)
    txt.font = 'Arial-55'
    window.add(txt)


if __name__ == '__main__':
    main()
