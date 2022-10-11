d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.SE, Length.short)
d.position_pen(1,0)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)

d.end()
