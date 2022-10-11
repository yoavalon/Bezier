d = DslBezier()

d.position_pen(1,1)
d.position_pen(3,1)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,2)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)

d.end()
