d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.curve(Direction.S, Orient.right, Length.short, Radius.high)
d.position_pen(1,2)
d.position_pen(1,0)
d.straight_line(Direction.S, Length.short)

d.end()
