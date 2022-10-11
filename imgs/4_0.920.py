d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,0)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)

d.end()
