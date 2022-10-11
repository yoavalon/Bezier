d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)

d.end()
