d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.W, Length.long)
d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)

d.end()
