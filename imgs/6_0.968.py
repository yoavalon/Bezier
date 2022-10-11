d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)

d.end()
