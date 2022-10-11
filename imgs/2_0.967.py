d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.S, Length.long)

d.end()
