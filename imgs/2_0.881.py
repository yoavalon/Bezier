d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.SE, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.NW, Length.long)
d.position_pen(1,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)

d.end()
