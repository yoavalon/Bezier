d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.E, Length.long)
d.position_pen(1,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)

d.end()
