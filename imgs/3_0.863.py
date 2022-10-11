d = DslBezier()

d.position_pen(2,0)
d.position_pen(2,0)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)

d.end()
