d = DslBezier()

d.position_pen(3,0)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.long)

d.end()
