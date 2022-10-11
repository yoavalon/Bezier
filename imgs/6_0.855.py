d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.SE, Orient.left, Length.long, Radius.low)

d.end()
