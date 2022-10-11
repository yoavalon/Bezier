d = DslBezier()

d.position_pen(3,0)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.position_pen(2,0)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.position_pen(2,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)

d.end()
