d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)

d.end()
