d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.SW, Length.long)

d.end()
