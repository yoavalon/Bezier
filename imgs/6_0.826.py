d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.high)
d.curve(Direction.NW, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.E, Length.short)
d.position_pen(3,1)
d.straight_line(Direction.NW, Length.long)
d.position_pen(3,3)

d.end()
