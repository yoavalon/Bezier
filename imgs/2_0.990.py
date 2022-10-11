d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,1)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.SW, Length.medium)

d.end()
