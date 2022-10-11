d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,0)
d.curve(Direction.SE, Orient.left, Length.short, Radius.high)

d.end()
