d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.position_pen(3,1)

d.end()
