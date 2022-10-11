d = DslBezier()

d.position_pen(2,0)
d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.E, Length.short)
d.position_pen(1,1)
d.straight_line(Direction.NE, Length.short)

d.end()
