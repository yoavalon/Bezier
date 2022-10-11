d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.SW, Length.short)
d.position_pen(3,1)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)
d.position_pen(1,3)
d.straight_line(Direction.S, Length.short)

d.end()
