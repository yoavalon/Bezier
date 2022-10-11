d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)

d.end()
