d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,1)

d.end()
