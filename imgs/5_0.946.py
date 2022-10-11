d = DslBezier()

d.position_pen(3,0)
d.position_pen(3,0)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.low)

d.end()
