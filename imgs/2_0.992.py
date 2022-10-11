d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.NE, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(2,1)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.SE, Orient.left, Length.long, Radius.low)

d.end()
