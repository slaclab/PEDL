import pedl
import pytest

def test_add_objects():
    p   = pedl.Widget()

    l   = pedl.layout.Layout()
    c_l = pedl.layout.Layout()
    c_l.widgets = [p]

    #Test Widget
    l.addWidget(p)
    assert l.widgets == [p]
    with pytest.raises(TypeError):
        l.addWidget(4)

    #Test Layout
    l.addLayout(c_l)
    assert l.widgets == [p,c_l]
    with pytest.raises(TypeError):
        l.addLayout(4)

    with pytest.raises(ValueError):
        l.addLayout(pedl.layout.Layout())

def test_spacing():
    l  = pedl.layout.Layout()
    assert l.spacing == 5
    l.spacing = 10
    assert l.spacing == 10

def test_alignment():
    l = pedl.layout.Layout()
    l.alignment = pedl.choices.AlignmentChoice.Left
    assert  l.alignment == pedl.choices.AlignmentChoice.Left


def test_horizontal_layout():
    l = pedl.HBoxLayout()
    
    assert l.w == 0
    assert l.h == 0

    l.addWidget(pedl.Widget(w=50,  h=100))
    l.addWidget(pedl.Widget(w=100, h=50))
    l.addWidget(pedl.Widget(w=100, h=100))

    #Default locations
    assert l.widgets[0].x == 0
    assert l.widgets[1].x == 55
    assert l.widgets[2].x == 160

    assert l.widgets[0].y == 0
    assert l.widgets[1].y == 0
    assert l.widgets[2].y == 0

    assert l.w == 260
    assert l.h == 100

    #Adjust Spacing
    l.spacing = 10
    assert l.widgets[0].x == 0
    assert l.widgets[1].x == 60
    assert l.widgets[2].x == 170
    assert l.w            == 270

    #Adjust Alignments
    l.alignment = pedl.choices.AlignmentChoice.Center
    assert l.widgets[0].y == 0
    assert l.widgets[1].y == 25
    assert l.widgets[2].y == 0
    assert l.h            == 100
    
    l.alignment = pedl.choices.AlignmentChoice.Left
    assert l.widgets[0].y == 0
    assert l.widgets[1].y == 25
    assert l.widgets[2].y == 0
    assert l.h            == 100
    
    l.alignment = pedl.choices.AlignmentChoice.Bottom
    assert l.widgets[0].y == 0
    assert l.widgets[1].y == 50
    assert l.widgets[2].y == 0
    assert l.h            == 100

    #Adjust Position
    l.x = 100
    l.y = 150

    assert l.widgets[0].x == 100
    assert l.widgets[1].x == 160
    assert l.widgets[2].x == 270
    assert l.w            == 270

    assert l.widgets[0].y == 150
    assert l.widgets[1].y == 200
    assert l.widgets[2].y == 150
    assert l.h            == 100

    assert l.x == 100
    assert l.y == 150

def test_vertical_layout():
    l = pedl.VBoxLayout()
    l.addWidget(pedl.Widget(w=50,  h=100))
    l.addWidget(pedl.Widget(w=100, h=50))
    l.addWidget(pedl.Widget(w=100, h=100))

    #Default locations
    assert l.widgets[0].x == 0
    assert l.widgets[1].x == 0
    assert l.widgets[2].x == 0

    assert l.widgets[0].y == 0
    assert l.widgets[1].y == 105
    assert l.widgets[2].y == 160

    assert l.w == 100
    assert l.h == 260

    #Adjust Spacing
    l.spacing = 10
    assert l.widgets[0].y == 0
    assert l.widgets[1].y == 110
    assert l.widgets[2].y == 170
    assert l.h            == 270

    #Adjust Alignments
    l.alignment = pedl.choices.AlignmentChoice.Center
    assert l.widgets[0].x == 0
    assert l.widgets[1].x == -25
    assert l.widgets[2].x == -25
    assert l.w            == 100
    
    l.alignment = pedl.choices.AlignmentChoice.Top
    assert l.widgets[0].x == 0
    assert l.widgets[1].x == -25
    assert l.widgets[2].x == -25
    assert l.w            == 100
    
    l.alignment = pedl.choices.AlignmentChoice.Right
    assert l.widgets[0].x == 0
    assert l.widgets[1].x == -50
    assert l.widgets[2].x == -50
    assert l.w            == 100

    #Adjust Position
    l.x = 100
    l.y = 150

    assert l.widgets[0].x == 150
    assert l.widgets[1].x == 100
    assert l.widgets[2].x == 100
    assert l.w            == 100

    assert l.widgets[0].y == 150
    assert l.widgets[1].y == 260
    assert l.widgets[2].y == 320
    assert l.h            == 270
    
    assert l.x == 100
    assert l.y == 150

def test_stack_layout():
    l = pedl.StackedLayout()
    l.addWidget(pedl.Widget(w=50,  h=100))
    l.addWidget(pedl.Widget(w=100, h=50))
    l.addWidget(pedl.Widget(w=100, h=100))

    #Default locations
    assert l.widgets[0].x == 0
    assert l.widgets[1].x == -25
    assert l.widgets[2].x == -25

    assert l.widgets[0].y == 0
    assert l.widgets[1].y == 25
    assert l.widgets[2].y == 0

    assert l.w == 100
    assert l.h == 100

    #Adjust Spacing
    assert l.spacing == None
    
    with pytest.raises(ValueError):
        l.spacing = 4

    #Adjust Alignments
    l.alignment = pedl.choices.AlignmentChoice.Left
    assert l.widgets[0].x == 0
    assert l.widgets[1].x == 0
    assert l.widgets[2].x == 0
    assert l.widgets[0].y == 0
    assert l.widgets[1].y == 25
    assert l.widgets[2].y == 0
    assert l.w            == 100
    assert l.h            == 100

    l.alignment = pedl.choices.AlignmentChoice.Top
    assert l.widgets[0].x == 0
    assert l.widgets[1].x == -25
    assert l.widgets[2].x == -25
    assert l.widgets[0].y == 0
    assert l.widgets[1].y == 0
    assert l.widgets[2].y == 0
    assert l.w            == 100
    assert l.h            == 100    
    
    l.alignment = pedl.choices.AlignmentChoice.Right
    assert l.widgets[0].x == 0
    assert l.widgets[1].x == -50
    assert l.widgets[2].x == -50
    assert l.widgets[0].y == 0
    assert l.widgets[1].y == 25
    assert l.widgets[2].y == 0
    assert l.w            == 100
    assert l.h            == 100    
    
    l.alignment = pedl.choices.AlignmentChoice.Bottom
    assert l.widgets[0].x == 0
    assert l.widgets[1].x == -25
    assert l.widgets[2].x == -25
    assert l.widgets[0].y == 0
    assert l.widgets[1].y == 50
    assert l.widgets[2].y == 0
    assert l.w            == 100
    assert l.h            == 100    
    
    l.alignment = (pedl.choices.AlignmentChoice.Top,
                   pedl.choices.AlignmentChoice.Right)
    assert l.widgets[0].x == 0
    assert l.widgets[1].x == -50
    assert l.widgets[2].x == -50
    assert l.widgets[0].y == 0
    assert l.widgets[1].y == 0
    assert l.widgets[2].y == 0
    assert l.w            == 100
    assert l.h            == 100    

    #Adjust Position
    l.x = 100
    l.y = 150

    assert l.widgets[0].x == 150
    assert l.widgets[1].x == 100
    assert l.widgets[2].x == 100
    assert l.w            == 100

    assert l.widgets[0].y == 150
    assert l.widgets[1].y == 150
    assert l.widgets[2].y == 150
    assert l.h            == 100
    
    assert l.x == 100
    assert l.y == 150

def test_compound_layout():
    h  = pedl.HBoxLayout()
    v1 = pedl.VBoxLayout()
    v2 = pedl.VBoxLayout()
    for l in (v1,v2):
        l.addWidget(pedl.Widget(w=100,h=200))
        l.addWidget(pedl.Widget(w=200,h=100))
        h.addLayout(l)

    #Check layout positioning
    assert h.widgets[0].x == 0
    assert h.widgets[1].x == 205
    assert h.widgets[0].y == 0
    assert h.widgets[1].y == 0
    assert h.w == 405
    assert h.h == 305

    #Move child alignment
    h.alignment = pedl.choices.AlignmentChoice.Bottom
    v1.spacing  = 30
    assert h.widgets[0].y == 0
    assert h.widgets[1].y == 25
    assert h.h == 330

    #Move parent alignment
    h.spacing  = 30
    assert h.widgets[0].x == 0
    assert h.widgets[1].x == 230
    assert h.w == 430



