d = DslBezier()

d.position_pen(2,0)
d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.N, Length.medium)
d.position_pen(0,1)
d.straight_line(Direction.NE, Length.long)

d.end()
