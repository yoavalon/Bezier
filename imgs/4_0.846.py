d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,1)
d.curve(Direction.SW, Orient.left, Length.short, Radius.high)
d.position_pen(1,0)
d.straight_line(Direction.SE, Length.short)
d.position_pen(2,1)

d.end()
