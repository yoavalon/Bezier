d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)

d.end()
