d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.S, Length.long)
d.position_pen(2,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.NW, Length.medium)

d.end()
