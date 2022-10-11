d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)

d.end()
