d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.position_pen(0,0)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)

d.end()
