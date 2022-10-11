d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.SW, Length.long)
d.position_pen(2,3)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.S, Length.long)

d.end()
