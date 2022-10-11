d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.position_pen(2,0)
d.position_pen(1,2)
d.straight_line(Direction.SE, Length.medium)

d.end()
