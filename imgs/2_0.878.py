d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,3)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,0)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,2)

d.end()
