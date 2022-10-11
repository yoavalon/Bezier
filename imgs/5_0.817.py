d = DslBezier()

d.position_pen(3,3)
d.straight_line(Direction.NE, Length.long)
d.position_pen(3,0)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,3)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.SW, Length.medium)

d.end()
