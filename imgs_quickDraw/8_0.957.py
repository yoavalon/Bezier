d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.W, Orient.left, Length.short, Radius.low)

d.end()
