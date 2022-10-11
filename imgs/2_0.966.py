d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(0,3)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)

d.end()
