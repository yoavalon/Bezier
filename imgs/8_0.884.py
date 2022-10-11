d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,1)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.W, Length.medium)

d.end()
