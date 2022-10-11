d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.position_pen(0,3)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)
d.position_pen(2,1)

d.end()
