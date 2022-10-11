d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,0)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,1)

d.end()
