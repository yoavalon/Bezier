d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.SE, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.E, Orient.left, Length.long, Radius.high)

d.end()
